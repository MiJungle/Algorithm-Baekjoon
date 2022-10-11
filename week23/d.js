// let car = {
//    color: 'red',
//    drive: function(){
//       const inner = function() {
//          console.log(this);
//       }
//       inner()
//    },
//    honk: function() {
//       const inner = () => {
//          console.log(this);
//       }
//       inner();
//    }
// }

// car.drive();
// car.honk();


// let obj = {
//    myVar: 'foo',
 
//    myFunc: function() {
//      console.log(this.myVar)
 
//      setTimeout(function() {
//        console.log(this)//여기서의 this는 window를 가르킴.
//      }, 1000)
//    }
//  }
//  obj.myFunc()// foo ... then... undefined

// var man = {
//    name: 'john',
//    hello: function() {
//        // 2. 객체이므로 this는 man을 가리킴
//        console.log(this.name);
//    }
// }
// hello(); // 3. hello john

// let obj = {
//   myVar: 'foo',

//   myFunc: function() {
// 		console.log(this.myVar)

//     setTimeout(function() {
//       console.log(this.myVar)
//     }.bind(this), 1000)
//   }
// }
// obj.myFunc()// foo ... then... foo

// (function () {
//    // 화살표 함수 foo의 arguments는 상위 스코프인 즉시 실행 함수의 arguments를 가리킨다.
//    const foo = () => console.log(arguments); // [Arguments] { '0': 1, '1': 2 }
//    foo(3, 4);
//  }(1, 2));
 
//  // 화살표 함수 foo의 arguments는 상위 스코프인 전역의 arguments를 가리킨다.
//  // 하지만 전역에는 arguments 객체가 존재하지 않는다. arguments 객체는 함수 내부에서만 유효하다.
//  const foo = () => console.log(arguments);
//  foo(1, 2); // ReferenceError: arguments is not defined

//  class Base {
//    constructor(name) {
//      this.name = name;
//    }
 
//    sayHi() {
//      return `Hi! ${this.name}`;
//    }
//  }
 
//  class Derived extends Base {
//    // 화살표 함수의 super는 상위 스코프인 constructor의 super를 가리킨다.
//    sayHi = () => `${super.sayHi()} how are you doing?`;
//  }
 
//  const derived = new Derived('Lee');
//  console.log(derived.sayHi()); // Hi! Lee how are you doing?

// const Foo = ()=> {
//    if (!new.target) { throw 'Foo() must be called with new' }
//    console.log('Foo instantiated with new')
//  }
 
//  new Foo()  // logs "Foo instantiated with new"
// //  Foo()      // throws "Foo() must be called with new"

// render() {
//    return(
//      <ChildComponent onChange={ this.handleChange.bind(this) } />
//    )
// }

// const person = {
//    name: 'Lee',
//    sayHi: () => console.log(`Hi ${this.name}`)
//  };
 
//  person.sayHi(); // Hi undefined
//  const person = {
//    name: 'Lee',
//  };
 
//  Object.prototype.sayHi = () => console.log(`Hi ${this.name}`);
 
//  person.sayHi(); // Hi undefined

//  const Foo = () => {};

// // 화살표 함수는 prototype 프로퍼티가 없다
// console.log(Foo.hasOwnProperty('prototype')); // false

// const foo = new Foo(); // TypeError: Foo is not a constructor
// 'use strict';
// let car = {
//    color: 'red',
//    drive: function(){
//       const inner = function(){
//          console.log(this);
//       }
//      inner()
//    }
// }
// car.drive()

class Base {
   constructor(name) {
     this.name = name;
   }
 
   sayHi() {
     return `Hi! ${this.name}`;
   }
 }
 
 var man = {
   name: 'john',
   hello: function() {
       // 2. 객체이므로 this는 man을 가리킴
       console.log('hello ' + this.name);
   }
}
man.hello(); // 3. hello john