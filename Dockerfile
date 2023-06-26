FROM  Python:3.8
RUN mkdir -p /app
COPY /etc/.config-api.json /etc/.config-api.json
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT [ "python" ]