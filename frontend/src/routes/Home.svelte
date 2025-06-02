<script>
  import fastapi from '../lib/api';
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

<ul>
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>
