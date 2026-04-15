import logging
import pytest 
import os

os.makedirs("screenshots", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

file_handler = logging.FileHandler("logs/test.log", mode="w", encoding="utf-8")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)