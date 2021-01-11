## Test Assignment for EDX
docker build -t cheque_writer:latest .

docker run -p 5010:5009 -ti cheque_writer:latest

##Usage

Test cases files are available in tests folder

test_cheque_writer.py [ Mix text cases for RESTful and Full Stack(Selenium)]

test_cheque_writer_RESTful.py[Only RESTful]

test_cheque_writer_full_stack.py[Only Full Stack]
