FROM python:3.11-slim

WORKDIR /app

COPY canbeshipped.py .
COPY digitalproduct.py .
COPY file.py .
COPY inventory_manager.py .
COPY inventory.py .
COPY order.py .
COPY orderline.py .
COPY physicalproduct.py .
COPY product.py .
COPY supplier.py .
COPY inventory.json .

CMD ["python", "inventory_manager.py"]