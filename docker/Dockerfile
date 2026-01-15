FROM bitnami/spark:3.5

# Set working directory
WORKDIR /app


# Copy application code
COPY spark/ /app/spark
COPY generator /app/generator
COPY configs /app/configs


# Install any additional dependencies if needed
RUN pip install -r requirements.txt


# Set the entrypoint to run the Spark application
CMD ["bash"]


