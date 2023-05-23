const goods = [
    {
        id: 1,
        name: "Товар 1",
        description: "Описание 1",
        sizes: ["s", "xs"],
        price: 1,
        available: true,  
    },
    {
        id: 2,
        name: "Товар 2",
        description: "Описание 2",
        sizes: ["xl", "xxl"],
        price: 1,
        available: true,  
    },
    {
        id: 3,
        name: "Товар 3",
        description: "Описание 3",
        sizes: ["xs", "l"],
        price: 1,
        available: true,  
    },
    {
        id: 4,
        name: "Товар 4",
        description: "Описание 4",
        sizes: ["xxs", "m"],
        price: 1000,
        available: false,  
    },
    {
        id: 5,
        name: "Товар 5",
        description: "Описание 5",
        sizes: ["s", "3xl"],
        price: 333,
        available: false,  
    },
];

let basket = [
    {
        good: 1,
        amount: 5,
    },
    {
        good: 3,
        amount: 2,
    },
];

function getGoodByID(id){
    let i = goods.findIndex(good => good.id === id);
    if (i < 0) return false;
    return goods[i];
}

function addToBasket(goodId, amount){
    let good = getGoodByID(goodId)
    if (!good || !good.available) return;

    let goodBasketI = basket.findIndex(good => good.good === goodId);
    if (goodBasketI >= 0){
        basket[goodBasketI].amount += amount;
    } else {
        basket.push({
            good: goodId,
            amount: amount,
        });
    }
}

function removeFromBasket(position){
    basket.splice(position, 1);
}

function clearBasket(){
    basket = []
}

function getStats(){
    return {
        totalAmount: basket.length,
        totalSumm: basket.reduce((sum, good) => sum + getGoodByID(good.good).price * good.amount, 0),
    };
}

clearBasket();
addToBasket(2, 5);
addToBasket(1, 5);
addToBasket(4, 1);
removeFromBasket(0);

console.log(getStats());

