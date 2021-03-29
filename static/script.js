 document.addEventListener('DOMContentLoaded', function() {

                let correct = document.querySelector('.correct');
                correct.addEventListener('click', function() {
                    correct.style.backgroundColor = 'green';
                    document.querySelector('#A1').innerHTML = 'Правильно';
            });

            let incorrects = document.querySelectorAll('.incorrect');
            for (let i = 0; i < incorrects.length; i++) {
                incorrects[i].addEventListener('click', function() {
                    incorrects[i].style.backgroundColor = 'red';
                    document.querySelector('#A1').innerHTML = 'Неправильно';

                });
            }
    
             document.querySelector('.check').addEventListener('click', function() {
                 let input = document.querySelector('input');
                 if (input.value === '17') {
                     input.style.backgroundColor = 'green';
                     document.querySelector('#A2').innerHTML = 'Правильно';
                 } else {
                     input.style.backgroundColor = 'red';
                     document.querySelector('#A2').innerHTML = 'Неправильно';
                 }
             });
           });
