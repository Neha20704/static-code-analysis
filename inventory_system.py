"""Inventory management system for tracking stock items."""
import json
from datetime import datetime


class InventorySystem:
    """Manages inventory stock data and operations."""

    def __init__(self):
        """Initialize the inventory system with empty stock data."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add items to the inventory.

        Args:
            item: Name of the item to add
            qty: Quantity to add
            logs: Optional list to store log messages
        """
        if logs is None:
            logs = []
        if not item:
            return

        # Input validation
        if not isinstance(item, str):
            print(f"Error: Item name must be a string, got "
                  f"{type(item).__name__}")
            return
        if not isinstance(qty, int) or qty < 0:
            print(f"Error: Quantity must be a non-negative integer, "
                  f"got {qty}")
            return

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove items from the inventory.

        Args:
            item: Name of the item to remove
            qty: Quantity to remove
        """
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Error: Item '{item}' not found in inventory")
        except TypeError as e:
            print(f"Error: Invalid operation - {e}")

    def get_qty(self, item):
        """Get the quantity of an item in inventory.

        Args:
            item: Name of the item

        Returns:
            Quantity of the item, or 0 if not found
        """
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file.

        Args:
            file: Path to the JSON file
        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.loads(f.read())
        except FileNotFoundError:
            print(f"Warning: File '{file}' not found. "
                  "Starting with empty inventory.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in '{file}'")

    def save_data(self, file="inventory.json"):
        """Save inventory data to a JSON file.

        Args:
            file: Path to the JSON file
        """
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.stock_data))

    def print_data(self):
        """Print the current inventory report."""
        print("Items Report")
        for item in self.stock_data:
            print(f"{item} -> {self.stock_data[item]}")

    def check_low_items(self, threshold=5):
        """Check for items below a quantity threshold.

        Args:
            threshold: Minimum quantity threshold

        Returns:
            List of items below the threshold
        """
        result = []
        for item in self.stock_data:
            if self.stock_data[item] < threshold:
                result.append(item)
        return result


def main():
    """Main execution function."""
    inventory = InventorySystem()

    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item(123, "ten")
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print(f"Apple stock: {inventory.get_qty('apple')}")
    print(f"Low items: {inventory.check_low_items()}")
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()
    # Removed eval - it's a security risk
    print("Operation completed")


if __name__ == "__main__":
    main()
