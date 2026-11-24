import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    """Calculate the total price of products."""

    if not isinstance(price, (int, float)) or isinstance(price, bool):
        logger.error("Invalid price type")
        raise TypeError("Price must be a number.")

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        logger.error("Invalid quantity type")
        raise TypeError("Quantity must be an integer.")

    if price <= 0:
        logger.error("Price must be greater than zero")
        raise ValueError("Price must be greater than zero.")

    if quantity <= 0:
        logger.error("Quantity must be greater than zero")
        raise ValueError("Quantity must be greater than zero.")

    total = price * quantity
    logger.info("Total price calculated successfully: %s", total)

    return total


def apply_discount(total, discount_percent):
    """Calculate the final price after discount."""

    if not isinstance(total, (int, float)) or isinstance(total, bool):
        logger.error("Invalid total type")
        raise TypeError("Total must be a number.")

    if not isinstance(discount_percent, (int, float)) or isinstance(
        discount_percent, bool
    ):
        logger.error("Invalid discount type")
        raise TypeError("Discount must be a number.")

    if total < 0:
        logger.error("Total cannot be negative")
        raise ValueError("Total cannot be negative.")

    if discount_percent < 0 or discount_percent > 100:
        logger.error("Invalid discount percentage")
        raise ValueError("Discount must be between 0 and 100.")

    discount = (total * discount_percent) / 100
    final_price = total - discount

    logger.info("Discount applied successfully: %s", final_price)

    return final_price


def check_stock(available_stock, requested_quantity):
    """Check whether the requested product quantity is available."""

    if not isinstance(available_stock, int) or isinstance(available_stock, bool):
        logger.error("Invalid available stock type")
        raise TypeError("Available stock must be an integer.")

    if not isinstance(requested_quantity, int) or isinstance(requested_quantity, bool):
        logger.error("Invalid requested quantity type")
        raise TypeError("Requested quantity must be an integer.")

    if available_stock < 0:
        logger.error("Available stock cannot be negative")
        raise ValueError("Available stock cannot be negative.")

    if requested_quantity <= 0:
        logger.error("Requested quantity must be positive")
        raise ValueError("Requested quantity must be greater than zero.")

    if requested_quantity <= available_stock:
        logger.info("Stock available")
        return "Stock available"

    logger.warning("Insufficient stock")
    return "Insufficient stock"
