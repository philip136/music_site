document.addEventListener('DOMContentLoaded', function() {
      const webSocketBridge = new channels.WebSocketBridge();
      const nl = document.querySelector("#notifylist");

      webSocketBridge.connect('/notifications/');
      webSocketBridge.listen(function(action, stream) {
        console.log("RESPONSE:", action);
        if(action.event == "New Notification") {
          var el = document.createElement("li");
          el.innerHTML = `New notification for <b>${action.username}</b> ${action.message}`;
          nl.appendChild(el);
        }
      })
      document.ws = webSocketBridge; /* for debugging */
    })