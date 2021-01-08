FROM python3.8
WORKDIR /code
copy . /code
RUN pip install -r requirements.txt
CMD ['python','-u','app.py']