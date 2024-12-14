function changeContent() {
    document.getElementById('userlogin').style.display = 'none';
    document.getElementById('usersignup').style.display = 'block';

     // Update the nav link text and functionality
    const toggleLink = document.querySelector('nav a.toggle');
    toggleLink.textContent = 'Sign In';
    toggleLink.setAttribute('onclick', 'showSignIn()');
  }
  
  function showSignIn() {
    document.getElementById('userlogin').style.display = 'block';
    document.getElementById('usersignup').style.display = 'none';

      // Update the nav link text and functionality
    const toggleLink = document.querySelector('nav a.toggle');
    toggleLink.textContent = 'Sign Up';
    toggleLink.setAttribute('onclick', 'changeContent()');
  }
  