from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .address.address_request_builder import AddressRequestBuilder
    from .bandwidth_usage.bandwidth_usage_request_builder import BandwidthUsageRequestBuilder
    from .checkout.checkout_request_builder import CheckoutRequestBuilder
    from .contact_sales.contact_sales_request_builder import ContactSalesRequestBuilder
    from .invoices.invoices_request_builder import InvoicesRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder
    from .plans.plans_request_builder import PlansRequestBuilder
    from .setup_intent.setup_intent_request_builder import SetupIntentRequestBuilder
    from .storage_usage.storage_usage_request_builder import StorageUsageRequestBuilder
    from .subscription.subscription_request_builder import SubscriptionRequestBuilder
    from .tax.tax_request_builder import TaxRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /billing/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/billing/v1", path_parameters)
    
    @property
    def address(self) -> AddressRequestBuilder:
        """
        The address property
        """
        from .address.address_request_builder import AddressRequestBuilder

        return AddressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bandwidth_usage(self) -> BandwidthUsageRequestBuilder:
        """
        The bandwidthUsage property
        """
        from .bandwidth_usage.bandwidth_usage_request_builder import BandwidthUsageRequestBuilder

        return BandwidthUsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkout(self) -> CheckoutRequestBuilder:
        """
        The checkout property
        """
        from .checkout.checkout_request_builder import CheckoutRequestBuilder

        return CheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contact_sales(self) -> ContactSalesRequestBuilder:
        """
        The contactSales property
        """
        from .contact_sales.contact_sales_request_builder import ContactSalesRequestBuilder

        return ContactSalesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invoices(self) -> InvoicesRequestBuilder:
        """
        The invoices property
        """
        from .invoices.invoices_request_builder import InvoicesRequestBuilder

        return InvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        The jobs property
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_methods(self) -> PaymentMethodsRequestBuilder:
        """
        The paymentMethods property
        """
        from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder

        return PaymentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plans(self) -> PlansRequestBuilder:
        """
        The plans property
        """
        from .plans.plans_request_builder import PlansRequestBuilder

        return PlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def setup_intent(self) -> SetupIntentRequestBuilder:
        """
        The setupIntent property
        """
        from .setup_intent.setup_intent_request_builder import SetupIntentRequestBuilder

        return SetupIntentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage_usage(self) -> StorageUsageRequestBuilder:
        """
        The storageUsage property
        """
        from .storage_usage.storage_usage_request_builder import StorageUsageRequestBuilder

        return StorageUsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscription(self) -> SubscriptionRequestBuilder:
        """
        The subscription property
        """
        from .subscription.subscription_request_builder import SubscriptionRequestBuilder

        return SubscriptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tax(self) -> TaxRequestBuilder:
        """
        The tax property
        """
        from .tax.tax_request_builder import TaxRequestBuilder

        return TaxRequestBuilder(self.request_adapter, self.path_parameters)
    

