# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.number.ordering_comparison import greater_than, less_than
from hamcrest.library.text.stringcontains import contains_string

from pages.rate_checker import RateChecker
from pages.base import Base
from pages.screenshot import Screenshot


# CHART AREA
@then(u'I should see the selected "{state_name}" above the Rate Checker chart')
@then(u'I should see the lender rate offered to "{state_name}" residents')
def step(context, state_name):
    # Get the location state displayed on page
    actual_text = context.rate_checker.get_chart_location()
    # If the location tracker is not available then "Alabama" is set by default
    try:
        assert_that(actual_text, equal_to('Alabama'))
    # Verify that displayed location matches the expected state
    except AssertionError:
        assert_that(actual_text, equal_to(state_name))


@then(u'I should see the chart faded out to indicate the data is out of date')
def step(context):
    is_faded = context.rate_checker.is_chart_faded()
    assert_that(is_faded, equal_to(True))


@then(u'I should see the chart active with new data')
def step(context):
    # Wait for the chart to load
    assert_that(context.rate_checker.is_chart_loaded(), equal_to(True))


# STATE
@given(u'I select "{state_name}" as State')
@when(u'I select "{state_name}" as State')
def step(context, state_name):
    # Wait for the chart to load
    assert_that(context.rate_checker.is_chart_loaded(), equal_to(True))
    
    context.rate_checker.set_location(state_name)
    # Wait for the chart to load
    assert_that(context.rate_checker.is_chart_loaded(), equal_to(True))


@then(u'I should see "{state_name}" as the selected location')
def step(context, state_name):
    current_Selection = context.rate_checker.get_location()
    
    try:
        assert_that(current_Selection, equal_to(state_name))        
    except:
        # If the location tracker is not available then "Alabama" is set by default
        assert_that(current_Selection, equal_to('Alabama'))


# TABS AND LINKS
@then(u'I should see the "{tab_text}" tab selected')
def step(context, tab_text):
    actual_text = context.rate_checker.get_active_tab_text()
    assert_that(actual_text, equal_to(tab_text))


@when(u'I click on the "{link_name}" link in the Rate Checker page')
@when(u'I click on the "{link_name}" tab in the Rate Checker page')
def step(context, link_name):
    # Click the requested link
    context.rate_checker.click_link_by_text(link_name)
