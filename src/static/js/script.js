

// Delete Django Ajax Call
function deleteInfo(id) {
    if (action != false) {
      $.ajax({
          url: '{% url "Delete_Info" %}',
          data: {
              'id': id,
          },
          dataType: 'json',
          success: function (data) {
              if (data.deleted) {
                $("#studentInfoTable #user-" + id).remove();
              }
          }
      });
    }
  }