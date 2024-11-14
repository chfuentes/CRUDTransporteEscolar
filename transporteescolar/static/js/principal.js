function mensaje(texto, tag) {
  icono = ""
  switch (tag) {
    case "success":
      icono = "success"
      break
    case "error":
      icono = "error"
      break
    case "info":
      icono = "info"
      break
    default:
      icono = "warning"
  }
  Swal.fire({
    position: "center",
    icon: icono,
    title: texto,
    showConfirmButton: false,
    timer: 1500
  });
}