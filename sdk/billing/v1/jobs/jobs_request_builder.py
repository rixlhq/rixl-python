from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cleanup_bandwidth_snapshots.cleanup_bandwidth_snapshots_request_builder import CleanupBandwidthSnapshotsRequestBuilder
    from .daily_bandwidth_calculation.daily_bandwidth_calculation_request_builder import DailyBandwidthCalculationRequestBuilder
    from .monthly_bandwidth_calculation.monthly_bandwidth_calculation_request_builder import MonthlyBandwidthCalculationRequestBuilder

class JobsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /billing/v1/jobs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JobsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/billing/v1/jobs", path_parameters)
    
    @property
    def cleanup_bandwidth_snapshots(self) -> CleanupBandwidthSnapshotsRequestBuilder:
        """
        The cleanupBandwidthSnapshots property
        """
        from .cleanup_bandwidth_snapshots.cleanup_bandwidth_snapshots_request_builder import CleanupBandwidthSnapshotsRequestBuilder

        return CleanupBandwidthSnapshotsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_bandwidth_calculation(self) -> DailyBandwidthCalculationRequestBuilder:
        """
        The dailyBandwidthCalculation property
        """
        from .daily_bandwidth_calculation.daily_bandwidth_calculation_request_builder import DailyBandwidthCalculationRequestBuilder

        return DailyBandwidthCalculationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_bandwidth_calculation(self) -> MonthlyBandwidthCalculationRequestBuilder:
        """
        The monthlyBandwidthCalculation property
        """
        from .monthly_bandwidth_calculation.monthly_bandwidth_calculation_request_builder import MonthlyBandwidthCalculationRequestBuilder

        return MonthlyBandwidthCalculationRequestBuilder(self.request_adapter, self.path_parameters)
    

