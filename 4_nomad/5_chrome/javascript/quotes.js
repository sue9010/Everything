const quotes = [
  {
    quote:
      "우리는 앞으로 2년 뒤에 닥쳐올 변화에 대해서는 과대평가하지만 10년 뒤에 올 변화는 과소평가하는 경향이 있다. 그렇다고 스스로를 나태함으로 이끌지는 마라.",
    author: "빌 게이츠",
  },
  {
    quote:
      "스무 살에 잘 생기지 못하고, 서른 살에 힘세지 않고, 마흔 살에 돈 못 벌고, 쉰 살에 현명하지 못하면, 결코 잘 생기거나, 힘세거나, 돈 벌거나, 현명해질 수 없다.",
    author: "조지 허버트",
  },
  {
    quote:
      "행복한 삶의 비밀은 올바른 관계를 형성하고 그것에 올바른 가치를 매기는 것이다.",
    author: "노먼 토머스",
  },
  {
    quote: "나만이 내 인생을 바꿀 수 있다. 아무도 날 대신해 해줄 수 없다.",
    author: "캐롤 베넷",
  },
  {
    quote: "젊은 날의 의무는 부패에 맞서는 것이다.",
    author: "커트 코베인",
  },
  {
    quote:
      "우리는 앞으로 2년 뒤에 닥쳐올 변화에 대해서는 과대평가하지만 10년 뒤에 올 변화는 과소평가하는 경향이 있다. 그렇다고 스스로를 나태함으로 이끌지는 마라.",
    author: "빌 게이츠",
  },
  {
    quote:
      "스무 살에 잘 생기지 못하고, 서른 살에 힘세지 않고, 마흔 살에 돈 못 벌고, 쉰 살에 현명하지 못하면, 결코 잘 생기거나, 힘세거나, 돈 벌거나, 현명해질 수 없다.",
    author: "조지 허버트",
  },
  {
    quote:
      "행복한 삶의 비밀은 올바른 관계를 형성하고 그것에 올바른 가치를 매기는 것이다.",
    author: "노먼 토머스",
  },
  {
    quote: "나만이 내 인생을 바꿀 수 있다. 아무도 날 대신해 해줄 수 없다.",
    author: "캐롤 베넷",
  },
  {
    quote: "젊은 날의 의무는 부패에 맞서는 것이다.",
    author: "커트 코베인",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

// console.log(Math.floor(Math.random() * quotes.length));

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
