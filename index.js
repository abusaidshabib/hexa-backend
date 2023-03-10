const express = require('express');
const cors = require('cors');
const { query } = require('express');
const app = express();
const port = process.env.PORT || 5000;
const { MongoClient, ServerApiVersion, ObjectId } = require('mongodb');
require('dotenv').config();

app.use(cors());
app.use(express.json());

const uri = process.env.DB_URI;
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverApi: ServerApiVersion.v1,
});

async function run() {
  try {

    const db = client.db("hexa_bazaar");
    const allProducts = db.collection("allProducts");
    const faq = db.collection("faq");
    const blogs = db.collection("blogs");
    const collection = db.collection("collection");
    const carousel = db.collection("carousel");
    const reviewData = db.collection("review");
    const userCollection = db.collection('user');


    app.get('/products', async (req, res) => {
      let query = {};
      const data = await allProducts.find(query).toArray();
      res.send(data)
    })

    app.get("/product/:id", async (req, res) => {
      const id = req.params.id;
      let query = { _id: new ObjectId(`${id}`) };
      const data = await allProducts.findOne(query);
      res.send(data);
    })

    app.get("/faq", async (req, res) => {
      const data = await faq.find().toArray();
      res.send(data)
    })

    app.get("/blogs", async (req, res) => {
      const data = await blogs.find().toArray();
      res.send(data)
    })

    app.get("/collections", async (req, res) => {
      const data = await collection.find().toArray();
      res.send(data);
    })

    app.get("/reviews", async (req, res) => {
      const data = await reviewData.find().toArray();
      res.send(data);
    })

    app.get("/collection/:name", async (req, res) => {
      const name = req.params.name
      const query = { collection: `${name}` }
      const data = await allProducts.find(query).toArray();
      res.send(data);
    })

    app.get("/carousel", async (req, res) => {
      const data = await carousel.find().toArray();
      res.send(data);
    })

    app.post('/user', async (req, res) => {
      const user = req.body;
      const query = {
        email: user.email
      }
      const oldUser = await userCollection.find(query).toArray();
      if (oldUser.length) {
        const message = "you have already login"
        return res.send({ acknowledge: false, message })
      }
      const result = await userCollection.insertOne(user);
      res.send(result);
    })
  }
  finally {

  }
}
run().catch(error => console.error(error))

app.get('/', async (req, res) => {
  res.send("Hexa bazaar running!")
})

app.listen(port, () => {
  console.log(`Hexa app running on port ${port}`)
})