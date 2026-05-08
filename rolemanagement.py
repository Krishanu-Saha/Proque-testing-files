import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://stg.proquro.ai/")
    page.get_by_role("link", name="Sign In").click()
    page.get_by_role("link", name="Securely Login With Email").click()
    page.get_by_role("textbox", name="Email").click()
    page.locator("div").nth(2).click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("mobpark@yopmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Avromandal12345@")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button").first.click()
    page.get_by_role("link", name="Role Management").click()
    page.get_by_role("button", name="+ Create New Role").click()
    page.get_by_role("textbox", name="e.g., Senior Procurement").click()
    page.get_by_role("textbox", name="e.g., Senior Procurement").fill("Data Engineer2")
    page.get_by_role("textbox", name="e.g., SR_PROC_OFF").click()
    page.get_by_role("textbox", name="e.g., SR_PROC_OFF").fill("DE-009")
    page.get_by_role("textbox", name="Describe the role's").click()
    page.get_by_role("textbox", name="Describe the role's").fill("This role is for Data Engineer")
    page.get_by_role("button", name="Create Role").click()
