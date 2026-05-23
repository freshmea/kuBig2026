# .NET Binding: pythonnet Class Library

C#으로 만든 `.dll` assembly를 Python wrapper package에서 사용하는 예제입니다.

## 빌드

.NET SDK가 설치되어 있어야 합니다.

```powershell
dotnet build HelloLibrary/HelloLibrary.csproj -c Release
```

## Python 준비

```powershell
pip install pythonnet
```

## 실행

```powershell
python use_dotnet_hello.py
```

## 수업 포인트

- C# 구현은 `.dll` assembly입니다.
- Python package `dotnet_hello`는 CLR loading과 C# class 호출을 감춥니다.
- `.pyi`는 Python 사용자에게 보이는 wrapper API를 설명합니다.
