const quickAddForm = document.querySelector("[data-quick-add]");
if (quickAddForm && quickAddForm.dataset.quickAdd === "true") {
  document.addEventListener("keydown", (event) => {
    if (event.key.toLowerCase() === "n" && !event.ctrlKey && !event.metaKey && !event.altKey) {
      event.preventDefault();
      document.querySelector("#todo-title")?.focus();
    }
  });
}
