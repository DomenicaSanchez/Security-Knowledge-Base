#!/bin/bash

# I need to monitor my webapp from external access, but idc my creds are random
files="$(grep -Rl 'RemoteCIDRValve' $CATALINA_HOME/conf $CATALINA_HOME/webapps || true)" && \
    for f in $files; do \
      sed -i 's/allow="127.0.0.0\/8,::1\/128"/allow="0.0.0.0\/0,::\/0"/' "$f"; \
    done

find $CATALINA_HOME -name "context.xml" -print0 | while IFS= read -r -d '' f; do \
      sed -i 's/<Context>/<Context sessionCookiePath="\/">/' "$f"; \
      sed -i '/<\/Context>/i\    <Valve className="org.apache.catalina.valves.PersistentValve"/>\n    <Manager className="org.apache.catalina.session.PersistentManager">\n        <Store className="org.apache.catalina.session.FileStore" directory="'"$CATALINA_HOME"'/temp/sessions"/>\n    </Manager>' "$f"; \
done

# not the same password on remote :)
sed -i '$i\
<role rolename="manager-gui"/>\
<role rolename="admin-gui"/>\
<user username="admin" password="7296e780-c21b-11f0-9a52-a357fb24b9e2" roles="manager-gui,admin-gui"/>\
' $CATALINA_HOME/conf/tomcat-users.xml

# Light side
cd $CATALINA_HOME/webapps/light && \
    javac -cp "$CATALINA_HOME/lib/*" $(find WEB-INF/classes -name "*.java")

# Dark side
cd $CATALINA_HOME/webapps/dark && \
    javac -cp "$CATALINA_HOME/lib/*" $(find WEB-INF/classes -name "*.java")


/usr/local/tomcat/bin/catalina.sh run

