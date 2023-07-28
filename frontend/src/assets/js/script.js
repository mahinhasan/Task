function toggleNavItems() {
  var navItems = document.getElementById('navItems');
  if (navItems.style.maxHeight) {
    navItems.style.maxHeight = null; // Remove the maximum height to show the navigation
  } else {
    navItems.style.maxHeight = navItems.scrollHeight + 'px'; // Set the maximum height to the actual height of the navigation
  }
}
