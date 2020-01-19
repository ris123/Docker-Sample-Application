FROM openjdk:latest
EXPOSE 8082
ADD target/hello-service.jar hello-service.jar
ENTRYPOINT ["java","-jar","hello-service.jar"]