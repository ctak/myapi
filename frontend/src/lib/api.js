const fastapi = (
  operation, // get, post, put, delete
  url, // e.g., /api/question/list
  params = {}, // e.g., { page: 1, keyword: "마크다운" }
  success_callback = null,
  failure_callback = null
) => {
  let method = operation.toLowerCase();
  let content_type = "application/json";
  let body = JSON.stringify(params); // fastapi() 를 콜할 때는 javascript 객체임.

  let _url = import.meta.env.VITE_SERVER_URL + url;
  if (method === "get") {
    _url += "?" + new URLSearchParams(params).toString();
    body = null; // GET 요청은 body가 없어야 함.
  }

  let options = {
    method,
    Headers: {
      "Content-Type": content_type,
    },
    body,
  };

  fetch(_url, options).then((response) => {
    response
      .json()
      .then((json) => {
        if (response.status >= 200 && response.status < 300) {
          if (success_callback) {
            success_callback(json);
          }
        } else {
          // 이 구문이 동작하는지는 일단 의문임.
          if (failure_callback) {
            failure_callback(json);
          } else {
            alert(JSON.stringify(json));
          }
        }
      })
      .catch((error) => {
        // 이 구문은 서버에서 돌아오는 값의 에러가 아닌가?
        alert(JSON.stringify(error));
      });
  });
};

export default fastapi;
