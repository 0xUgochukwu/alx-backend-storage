-- creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER reduce_quantity
AFTER INSERT on orders
FOR EACH ROW
  UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
