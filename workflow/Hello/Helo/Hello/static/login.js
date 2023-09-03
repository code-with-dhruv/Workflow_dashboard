const users = [
    { username: 'dhruv', password: 'password' },
    { username: 'user2', password: 'password2' },
    // Add more users as needed
  ];
  
  const loginForm = document.getElementById('login-form');
  loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
  
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
  
    const username = usernameInput.value;
    const password = passwordInput.value;
  
    const user = users.find(user => user.username === username);
  
    if (user && user.password === password) {
      alert('Login successful!');
      window.location.href = '/';
    } else {
      alert('Invalid username or password. Please try again.');
    }
  
    // Clear input fields after login attempt
    usernameInput.value = '';
    passwordInput.value = '';
  });
  