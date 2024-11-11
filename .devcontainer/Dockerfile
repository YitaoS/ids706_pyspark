FROM python:3.9

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir black flake8 pytest

COPY . /workspace

CMD ["bash"]
