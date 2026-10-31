FROM python:3.11-slim

WORKDIR /app

COPY inventory_manager.py .
COPY inventory.py .
COPY file.py .
COPY product.py .
COPY inventory.json .

CMD ["python", "inventory_manager.py"]