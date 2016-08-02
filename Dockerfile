FROM python:3-onbuild

ADD saveFeeds.py /home/saveFeeds.py

EXPOSE 80

WORKDIR /home

CMD [ "python", "/home/saveFeeds.py" ]