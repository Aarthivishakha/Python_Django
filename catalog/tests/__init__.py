from __future__ import unicode_literals

from catalog.tests.test_models import ProductModelTests
from catalog.tests.test_pricing import CalculateOrderTotalTests, ClassifyOrderSizeTests
from catalog.tests.test_views import ViewTests

__all__ = [
    'ProductModelTests',
    'CalculateOrderTotalTests',
    'ClassifyOrderSizeTests',
    'ViewTests',
]
