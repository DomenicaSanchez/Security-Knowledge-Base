FROM eclipse-temurin:17-jdk

ENV CATALINA_HOME=/usr/local/tomcat
ENV PATH="$CATALINA_HOME/bin:$PATH"
ENV TOMCAT_VERSION=10.1.49

RUN mkdir -p $CATALINA_HOME && \
    apt-get update && apt-get install -y curl && \
    curl -fsSL https://dlcdn.apache.org/tomcat/tomcat-10/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz \
      | tar -xz -C $CATALINA_HOME --strip-components=1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY light $CATALINA_HOME/webapps/light
COPY dark $CATALINA_HOME/webapps/dark

COPY run.sh /
RUN chmod +x /run.sh

EXPOSE 8080

CMD ["/run.sh"]
