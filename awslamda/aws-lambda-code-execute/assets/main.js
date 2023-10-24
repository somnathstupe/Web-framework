// globals
const editor = ace.edit('editor');

$(function() {
  // configure ace editor
  editor.setTheme("ace/theme/monokai");
  editor.getSession().setMode("ace/mode/python");
  editor.setFontSize('14px');
});

// handle form submit
$('form').on('submit', (event) => {
  event.preventDefault();
  const answer = editor.getSession().getValue();
  const payload = { answer: answer };
  grade(payload);
});

// ajax request
function grade(payload) {
  $.ajax({
    method: 'POST',
    url: 'https://9iqv1loaic.execute-api.ap-south-1.amazonaws.com/dev',
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify(payload)
  })
  .done((res) => {
    let message = 'Incorrect. Please try again.';
    if (res) {
      message = 'Correct!';
    }
    $('.answer').html(message);
    console.log(res);
    console.log(message);
  })
  .catch((err) => {
    $('.answer').html('Something went terribly wrong!');
    console.log(err);
  });
}
