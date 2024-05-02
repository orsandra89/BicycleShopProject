FROM python:3.9-buster

# copy source and install dependencies
RUN python -m pip install --upgrade pip
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
# RUN mkdir -p /opt/app/bicycle-shop-project
COPY requirements.txt start-server.sh manage.py __init__.py /opt/app/
COPY BicycleShopProject /opt/app/BicycleShopProject
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app
RUN chmod +x /opt/app/start-server.sh

# start server
EXPOSE 8030
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
