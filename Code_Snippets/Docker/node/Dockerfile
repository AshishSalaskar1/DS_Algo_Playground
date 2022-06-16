FROM node:alpine

WORKDIR /usr/nodeapp

# COPY src dest(container)
# COPY  ./ <- current folder ./ <- WORKDIR
COPY ./ ./
RUN npm install

CMD ["npm", "start"]