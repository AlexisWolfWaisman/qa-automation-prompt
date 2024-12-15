from name_checker_api_tests import NameCheckerAPI

def run_diagnose():
    name_checker = NameCheckerAPI()
    name_checker.diagnose_system_errors()

if __name__ == "__main__":
    run_diagnose()
