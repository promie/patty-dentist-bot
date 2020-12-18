const msgerForm = get('.msger-inputarea')
const msgerInput = get('.msger-input')
const msgerChat = get('.msger-chat')
const msgInfoTime = get('.msg-info-time')

// Icons made by Freepik from www.flaticon.com
const BOT_IMG = 'https://image.flaticon.com/icons/svg/327/327779.svg'
const PERSON_IMG = 'https://image.flaticon.com/icons/svg/145/145867.svg'
const BOT_NAME = 'PATTY'
const PERSON_NAME = 'YOU'

msgerForm.addEventListener('submit', (event) => {
  event.preventDefault()

  const msgText = msgerInput.value
  if (!msgText) return

  appendMessage(PERSON_NAME, PERSON_IMG, 'right', msgText)
  msgerInput.value = ''

  botResponse(msgText)
})

msgInfoTime.textContent = formatDate(new Date())

function appendMessage(name, img, side, text) {
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `

  msgerChat.insertAdjacentHTML('beforeend', msgHTML)
  msgerChat.scrollTop += 500
}

function botResponse(expression) {
  const delay = expression.length * 100
  setTimeout(() => {
    fetch(`http://127.0.0.1:5000/api/v1/ask?expression=${expression}`)
      .then((response) => response.json())
      .then((data) => {
        appendMessage(BOT_NAME, BOT_IMG, 'left', data.answer)
      })
  }, delay)
}

function get(selector, root = document) {
  return root.querySelector(selector)
}

function formatDate(date) {
  const h = '0' + date.getHours()
  const m = '0' + date.getMinutes()

  return `${h.slice(-2)}:${m.slice(-2)}`
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min)
}
