<script>
  import fastapi from '../lib/api';
  import { link } from 'svelte-spa-router';

  let question_list = [];

  function get_question_list() {
  //   fetch('http://localhost:8000/api/question/list')
  //     .then(response => response.json())
  //     .then(data => {
  //       question_list = data;
  //     })
  //     .catch(error => {
  //       console.error('Error fetching questions:', error);
  //     });
      fastapi('get', '/api/question/list', {}, (json) => {
          question_list = json;
        })
  }

  get_question_list();
</script>

<div class="container my-3">
  <table class="table">
    <thead>
      <tr class="table-dark">
        <th>번호</th>
        <th>제목</th>
        <th>작성일시</th>
      </tr>
    </thead>
    <tbody>
      {#each question_list as question}
        <tr>
          <td>{question.id}</td>
          <td><a use:link href="/detail/{question.id}">{question.subject}</a></td>
          <td>{question.create_date}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
