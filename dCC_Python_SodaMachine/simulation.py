from customer import Customer
from soda_machine import SodaMachine
import user_interface


class Simulation:
    def __init__(self):
        pass

    @staticmethod
    def run_simulation():
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        soda_machine.fill_register()
        soda_machine.fill_inventory()
        customer.wallet.fill_wallet()
        while True:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
                customer.check_backpack()
            elif user_option == 4:
                quit()
