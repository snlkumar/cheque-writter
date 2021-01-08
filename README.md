docker build -t cheque_writer:latest .
docker run -p 5010:5009 -ti cheque_writer:latest