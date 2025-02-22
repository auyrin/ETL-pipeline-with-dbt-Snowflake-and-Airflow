select
    *
from
    {{ref('fct_orders')}}
where
    item_discount_amount > 0

-- this test makes sure our discounts are reducing the price and not increasing it