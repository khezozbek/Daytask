// main.js
document.addEventListener("DOMContentLoaded", function() {
  // Get the list of tasks
  var tasks = document.getElementsByClassName("task");

  // Get the current time
  var currentTime = new Date();

  // Loop through the tasks and check the completion time
  for (var i = 0; i < tasks.length; i++) {
    var task = tasks[i];
    var taskTimeStr = task.querySelector("span:last-child").textContent;
    var taskTime = new Date(taskTimeStr);

    // Set the completion time to the current date with task's completion time
    var completionTime = new Date(currentTime.toDateString() + " " + taskTimeStr);

    // Compare the current time with the task completion time
    if (currentTime >= completionTime) {
      // Display the task notification
      var notification = document.getElementById("notification");
      notification.textContent = "It's time to perform the task: " + task.querySelector("span:first-child").textContent;
      break; // Stop checking further tasks
    }
  }
});
