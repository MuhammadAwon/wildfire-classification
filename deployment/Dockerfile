# AWS lambda base image
FROM public.ecr.aws/lambda/python:3.9


# Install Keras image helper and TFLite runtime for AWS linux architecture
RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl

# Copy required files
COPY [ "wildfire-model.tflite", "lambda_function.py", "./"]

# Expose port
EXPOSE 8080

# Command to invoke lambda
CMD [ "lambda_function.lambda_handler" ]