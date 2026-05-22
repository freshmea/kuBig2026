# pip install pywebview

import webview


class Api:
    def make_gugudan(self, dan):
        try:
            dan = int(dan)
        except ValueError:
            return {
                "ok": False,
                "message": "숫자를 입력하세요.",
            }

        if dan < 1 or dan > 99:
            return {
                "ok": False,
                "message": "1부터 99 사이의 숫자를 입력하세요.",
            }

        lines = []
        for i in range(1, 10):
            lines.append(f"{dan} x {i} = {dan * i}")

        return {
            "ok": True,
            "title": f"{dan}단",
            "lines": lines,
        }


html = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <title>구구단 출력기</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background: #f5f5f5;
    }

    .container {
      max-width: 420px;
      margin: 0 auto;
      background: white;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    }

    h1 {
      margin-top: 0;
    }

    input {
      width: 100%;
      box-sizing: border-box;
      padding: 10px;
      font-size: 16px;
      margin-bottom: 12px;
    }

    button {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      cursor: pointer;
    }

    #result {
      margin-top: 20px;
      line-height: 1.8;
      font-size: 18px;
    }

    .error {
      color: crimson;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>구구단 출력기</h1>

    <input id="danInput" type="number" placeholder="몇 단을 출력할까요? 예: 7" />
    <button onclick="showGugudan()">출력</button>

    <div id="result"></div>
  </div>

  <script>
    async function showGugudan() {
      const dan = document.getElementById("danInput").value;
      const result = document.getElementById("result");

      const response = await window.pywebview.api.make_gugudan(dan);

      result.innerHTML = "";

      if (!response.ok) {
        result.innerHTML = `<div class="error">${response.message}</div>`;
        return;
      }

      let html = `<h2>${response.title}</h2>`;

      for (const line of response.lines) {
        html += `<div>${line}</div>`;
      }

      result.innerHTML = html;
    }

    document.getElementById("danInput").addEventListener("keydown", function(event) {
      if (event.key === "Enter") {
        showGugudan();
      }
    });
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    api = Api()

    webview.create_window(
        title="구구단 출력기",
        html=html,
        js_api=api,
        width=500,
        height=600,
    )

    webview.start()
