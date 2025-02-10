const todoList = [{
  name: 'make dinner',
  dueDate: '2025-12-22'
}, {
  name: 'wash dishes',
  dueDate: '2025-12-23'
}];

renderTodoList();

function renderTodoList() {

  let todoListHTML = '';

  todoList.forEach((todoObject, index) => {
    const { name, dueDate } = todoObject;
    
    const html = `
      <p>"${name}" ${dueDate}
        <button 
        class="js-delete-todo-button"  >Delete</button>
      </p>
    `;
    todoListHTML += html;
  })

  // for (let i = 0; i < todoList.length; i++) {
  //   const todoObject = todoList[i];
  //   // const name = todoObject.name;
  //   // const dueDate = todoObject.dueDate;
  //   const { name, dueDate } = todoObject;
    
  //   const html = `
  //     <p>"${name}" ${dueDate}
  //       <button onclick = "
  //         todoList.splice(${i}, 1);
  //         renderTodoList();
  //       ">Delete</button>
  //     </p>
  //   `;
  //   todoListHTML += html;
  // }
  console.log(todoListHTML);

  document.querySelector('.js-todo-list')
    .innerHTML = todoListHTML;

  document.querySelectorAll('.js-delete-todo-button')
    .forEach((deleteButton, index) => {
      deleteButton.addEventListener('click', () => {
        console.log(index);
        todoList.splice(index, 1);
        renderTodoList();
      })
    })

  // console.log(index) here it says that index doesn't exist, that is because the index instantly gets deleted right after the forEach loop ends, but if we move this consolelog inside the forEach, it gives out the value of index


  // this feature or property is called "Closure", if a function has access to a value, it always has access to that value,
  // value gets packaged together (enclosed) with the function
}

document.querySelector('.js-add-todo-button')
  .addEventListener('click', () => {
    addTodo();
  });


function addTodo() {
  const inputElement = document.querySelector('.js-name-input');
  const name = inputElement.value;

  const dateInputElement = document.querySelector('.js-date-input');
  const dueDate = dateInputElement.value;
  
  todoList.push({
    //name: name,
    //dueDate: dueDate,
    name,
    dueDate,
  });
  console.log(todoList);

  inputElement.value = '';
  renderTodoList();
}

