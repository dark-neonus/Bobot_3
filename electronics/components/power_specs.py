from enum import Enum
from typing import Optional, Tuple


class DeviceType(Enum):
    """Categorizes the role of a component in circuit validation DRC checks."""

    SUPPLY = "supply"
    CONDUCTOR = "conductor"
    CONSUMER = "consumer"


class VoltageSpec:
    """Represents voltage specifications for a component or power rail with read-only properties."""

    def __init__(self, min_v: float, rated_v: float, max_v: float):
        self._min_v = float(min_v)
        self._rated_v = float(rated_v)
        self._max_v = float(max_v)

    @property
    def min_v(self) -> float:
        """Minimum allowable voltage in Volts."""
        return self._min_v

    @property
    def rated_v(self) -> float:
        """Nominal operational voltage in Volts."""
        return self._rated_v

    @property
    def max_v(self) -> float:
        """Maximum allowable voltage in Volts."""
        return self._max_v

    @classmethod
    def from_tuple(
        cls, v_range: Tuple[float, float], rated_v: Optional[float] = None
    ) -> "VoltageSpec":
        """Constructs VoltageSpec from a (min_v, max_v) tuple."""
        min_val, max_val = v_range
        rated = rated_v if rated_v is not None else (min_val + max_val) / 2.0
        return cls(min_v=min_val, rated_v=rated, max_v=max_val)

    @property
    def values(self) -> Tuple[float, float, float]:
        """Returns (min_v, rated_v, max_v) tuple."""
        return (self._min_v, self._rated_v, self._max_v)

    def is_compatible(self, supply_v: float) -> bool:
        """Checks whether a given supply voltage falls within operating boundaries."""
        return self._min_v <= supply_v <= self._max_v


class CurrentSpec:
    """Represents current capability or draw specifications with device role categorization."""

    def __init__(
        self,
        rated_i: float,
        peak_i: float,
        device_type: DeviceType = DeviceType.CONSUMER,
    ):
        self._rated_i = float(rated_i)
        self._peak_i = float(peak_i)
        self._device_type = device_type

    @property
    def rated_i(self) -> float:
        """Continuous nominal current in Amperes."""
        return self._rated_i

    @property
    def peak_i(self) -> float:
        """Maximum peak/stall current in Amperes."""
        return self._peak_i

    @property
    def device_type(self) -> DeviceType:
        """Role of the component (SUPPLY, CONDUCTOR, or CONSUMER)."""
        return self._device_type

    @classmethod
    def from_single(
        cls,
        max_i: float,
        rated_ratio: float = 0.8,
        device_type: DeviceType = DeviceType.CONSUMER,
    ) -> "CurrentSpec":
        """Factory method for components defined primarily by a single current limit."""
        return cls(
            rated_i=float(max_i * rated_ratio),
            peak_i=float(max_i),
            device_type=device_type,
        )

    @property
    def values(self) -> Tuple[float, float]:
        """Returns (rated_i, peak_i) tuple."""
        return (self._rated_i, self._peak_i)

    def can_supply(self, required_i: float) -> bool:
        """Checks if peak current capacity covers a required load."""
        return self._peak_i >= required_i


class PowerSpec:
    """Combines VoltageSpec and CurrentSpec to calculate power metrics and perform DRC checks."""

    def __init__(self, voltage: VoltageSpec, current: CurrentSpec):
        self._voltage = voltage
        self._current = current

    @property
    def voltage(self) -> VoltageSpec:
        """Read-only access to VoltageSpec."""
        return self._voltage

    @property
    def current(self) -> CurrentSpec:
        """Read-only access to CurrentSpec."""
        return self._current

    @property
    def device_type(self) -> DeviceType:
        """Convenience property for accessing component DeviceType role."""
        return self._current.device_type

    @property
    def rated_power(self) -> float:
        """Calculates continuous nominal power in Watts (P_rated = V_rated * I_rated)."""
        return self._voltage.rated_v * self._current.rated_i

    @property
    def peak_power(self) -> float:
        """Calculates maximum peak power in Watts (P_peak = V_max * I_peak)."""
        return self._voltage.max_v * self._current.peak_i

    def is_voltage_compatible(self, source_voltage: float) -> bool:
        """Checks if a supply voltage is within this component's acceptable range."""
        return self._voltage.is_compatible(source_voltage)

    def can_supply_current(self, load_current: float) -> bool:
        """Checks if peak output current covers the load demand."""
        return self._current.can_supply(load_current)
