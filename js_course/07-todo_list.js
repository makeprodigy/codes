const todolist = [{
  name: 'make dinner',
  dueDate: '2025-12-22'
}, {
  name: 'wash dishes',
  dueDate: '2025-12-23'
}];

renderTodoList();

function renderTodoList() {

  let todolistHTML = '';

  for (let i = 0; i < todolist.length; i++) {
    const todoObject = todolist[i];
    // const name = todoObject.name;
    // const dueDate = todoObject.dueDate;
    const { name, dueDate } = todoObject;
    
    const html = `
      <p>"${name}" ${dueDate}
        <button onclick = "
          todolist.splice(${i}, 1);
          renderTodoList();
        ">Delete</button>
      </p>
    `;
    todolistHTML += html;
  }
  console.log(todolistHTML);

  document.querySelector('.js-todo-list')
    .innerHTML = todolistHTML;

}


function addTodo() {
  const inputElement = document.querySelector('.js-name-input');
  const name = inputElement.value;

  const dateInputElement = document.querySelector('.js-date-input');
  const dueDate = dateInputElement.value;
  
  todolist.push({
    //name: name,
    //dueDate: dueDate,
    name,
    dueDate,
  });
  console.log(todolist);

  inputElement.value = '';
  renderTodoList();
}

