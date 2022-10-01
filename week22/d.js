let a = {
    "id": "1",
    "title": "Back-end 협업 선호도 조사",
    "description": "Back-end가 어떤 기술로 구성하는 것을 선호하십니까?",
    "steps": [
      [
        {
          "type": "text",
          "label": "당신의 이름은?",
          "validation": {
            "isRequired": true
          }
        }
      ],
      [
        {
          "name": "prefer",
          "type": "singleChoice",
          "label": "다음중 가장 선호하는 Back-end 연동 방식은?",
          "options": [
            "RESTful API",
            "GraphQL",
            "RPC",
            "그외"
          ]
        }
      ]
    ]
  }
  
  for(let i =0 ; i <a.steps.length;i++){
    let k = a.steps[i][0].label
    console.log(k)
  }

  console.log(a.steps.length)