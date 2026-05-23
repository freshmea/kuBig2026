# Java Binding: JPype Jar

Java로 만든 `.jar` 파일을 Python wrapper package에서 사용하는 예제입니다.

이 방식은 Python extension module을 빌드하는 것이 아니라, Python 프로세스 안에서 JVM을 시작하고 Java class를 호출합니다.

## 빌드

JDK가 설치되어 있어야 합니다.

```powershell
javac -d build/classes src/main/java/com/example/HelloService.java
jar --create --file build/hello-service.jar -C build/classes .
```

## Python 준비

```powershell
pip install jpype1
```

## 실행

```powershell
python use_java_hello.py
```

## 수업 포인트

- Java 구현은 `.jar`입니다.
- Python package `java_hello`는 JVM 시작, class loading, method call을 감춥니다.
- `.pyi`는 Java object를 감싼 Python API를 설명합니다.
